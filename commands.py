from fastapi_interactions.commands import CommandRouter, Option
from fastapi_interactions.responses import MessageResponse

router = CommandRouter()


@router.command(name="greet", description="Greet someone")
@Option.string(name="name", description="Who to greet", required=True)
async def greet(ctx, name: str):
    return MessageResponse(f"Hello, {name}! 👋", ephemeral=False)


@router.command(name="rate", description="Rate something from 1 to 10")
@Option.integer(name="score", description="Rating", required=True)
async def rate(ctx, score: int):
    if score < 1 or score > 10:
        return MessageResponse("Score must be between 1 and 10", ephemeral=True)
    return MessageResponse(f"Rating: {score}/10 ⭐", ephemeral=False)


@router.command(name="toggle", description="Toggle a setting")
@Option.boolean(name="enabled", description="Enable or disable", required=True)
async def toggle(ctx, enabled: bool):
    status = "enabled ✅" if enabled else "disabled ❌"
    return MessageResponse(f"Setting is now {status}", ephemeral=True)


@router.command(name="profile", description="View someone's profile")
@Option.user(name="user", description="User to profile", required=True)
async def profile(ctx, user: str):
    return MessageResponse(f"Profile for <@{user}>", ephemeral=False)


@router.command(name="assign", description="Assign a role to someone")
@Option.mentionable(name="target", description="User or role", required=True)
@Option.role(name="role", description="Role to assign", required=True)
async def assign(ctx, target: str, role: str):
    return MessageResponse(
        f"Assigning <@&{role}> to <@&{target}>",
        ephemeral=True
    )


@router.command(name="info", description="Get bot info")
async def info(ctx):
    return MessageResponse(
        f"**Bot Info**\n"
        f"Invoked by: {ctx.user.username}\n"
        f"Guild: {ctx.guild_id or 'DM'}\n"
        f"Channel: {ctx.channel_id or 'N/A'}",
        ephemeral=True
    )
